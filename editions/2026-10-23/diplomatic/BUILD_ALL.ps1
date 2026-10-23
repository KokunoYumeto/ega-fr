param(
 [Parameter(Mandatory=$true)][string]$PdfLatex,
 [Parameter(Mandatory=$true)][string]$BibTeX,
 [Parameter(Mandatory=$true)][string]$Python,
 [Parameter(Mandatory=$true)][string]$OutputDirectory,
 [ValidateSet('native','direct')][string]$SourceForm='native',
 [hashtable]$ReusePrimaryDirectories=@{}
)
$ErrorActionPreference='Stop'
$root=[IO.Path]::GetFullPath($PSScriptRoot)
$output=[IO.Path]::GetFullPath($OutputDirectory)
if(Test-Path -LiteralPath $output){throw 'Fresh output directory required'}
$manifest=Get-Content -LiteralPath (Join-Path $root 'SOURCE_MANIFEST.json') -Raw|ConvertFrom-Json
foreach($entry in $manifest.files){
 $p=Join-Path $root $entry.path
 if((Get-Item -LiteralPath $p).Length -ne $entry.bytes -or (Get-FileHash -LiteralPath $p).Hash -ne $entry.sha256){throw "Source mismatch: $($entry.path)"}
}
$owned=$false;$abandoned=$false;$failure=$null;$completed=@()
$savedTemp=$env:TEMP;$savedTmp=$env:TMP
$slot=[Threading.Mutex]::new($false,'Global\InterlanguageTeXSlotV1')
[IO.Directory]::CreateDirectory($output)|Out-Null
$tempDirectory=Join-Path $output 'tmp'
[IO.Directory]::CreateDirectory($tempDirectory)|Out-Null
$env:TEMP=$tempDirectory;$env:TMP=$tempDirectory
try{
 try{$owned=$slot.WaitOne(1000)}catch [Threading.AbandonedMutexException]{$owned=$true;$abandoned=$true}
 if(-not $owned){throw 'TeX slot unavailable; no worker launched'}
 foreach($unit in @('BASE','IV1','IV2','IV3','IV4','COVER')){
  & (Join-Path $root "packages/$unit/BUILD.ps1") -PdfLatex $PdfLatex -BibTeX $BibTeX -SourceForm $SourceForm -OutputDirectory (Join-Path $output $unit) -ReusePrimaryDirectory ([string]$ReusePrimaryDirectories[$unit])
  $resultPath=Join-Path $output "$unit/BUILD_RESULT.json"
  $result=Get-Content -LiteralPath $resultPath -Raw|ConvertFrom-Json
  if(-not $result.acquired -or $result.error){throw "Build failed: $unit"}
  $completed+=@{unit=$unit;result=$resultPath}
 }
 foreach($edition in @('primary','replay')){
  $arguments=@('-X','utf8',(Join-Path $root 'reconstruction/assemble.py'),'--components')
  foreach($unit in @('BASE','IV1','IV2','IV3','IV4')){
   $config=Get-Content -LiteralPath (Join-Path $root "packages/$unit/BUILD_CONFIG.json") -Raw|ConvertFrom-Json
   $arguments+=Join-Path $output "$unit/$edition/$($config.job_name).pdf"
  }
  $arguments+=@('--cover',(Join-Path $output "COVER/$edition/EGA_French_Cover.pdf"),'--legacy',(Join-Path $root 'reconstruction/LEGACY_ALIASES.json'),'--metadata',(Join-Path $root 'reconstruction/METADATA.json'),'--output',"EGA_French_Cumulative_$edition.pdf")
  $guardPath=Join-Path $output "assembly_$edition.guard.json"
  & (Join-Path $root 'packages/BASE/build_support/run_guarded_process.ps1') -FilePath $Python -ArgumentList $arguments -WorkingDirectory $output -TaskRoot $output -ReceiptPath $guardPath -TimeoutSeconds 1200|Out-Null
  $guard=Get-Content -LiteralPath $guardPath -Raw|ConvertFrom-Json
  if($guard.status -ne 'SUCCEEDED' -or $guard.cap_triggered -or $guard.memory_limit_bytes -ne 3221225472 -or $guard.final_active_processes -ne 0){throw 'Assembly process guard failed'}
 }
 $a=Join-Path $output 'EGA_French_Cumulative_primary.pdf'
 $b=Join-Path $output 'EGA_French_Cumulative_replay.pdf'
 if((Get-FileHash -LiteralPath $a).Hash -ne (Get-FileHash -LiteralPath $b).Hash){throw 'Cumulative replay differs'}
 # Standalone cross-volume links use this exact companion filename.
 [IO.File]::Copy($a,(Join-Path $output 'EGA_French_Diplomatic_Cumulative_Reader.pdf'),$false)
}catch{$failure=$_.Exception.Message}
finally{
 if($owned){$slot.ReleaseMutex()};$slot.Dispose()
 $env:TEMP=$savedTemp;$env:TMP=$savedTmp
 $record=@{source_form=$SourceForm;acquired=$owned;abandoned=$abandoned;completed=$completed;error=$failure;publication=$false;qa='Separate source-bound semantic and visual review still required'}
 [IO.File]::WriteAllText((Join-Path $output 'BUILD_ALL_RESULT.json'),($record|ConvertTo-Json -Depth 6)+"`n",[Text.UTF8Encoding]::new($false))
}
if($failure){throw $failure}
