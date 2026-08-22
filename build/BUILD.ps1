$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $repoRoot 'source'
$outputRoot = Join-Path $PSScriptRoot 'out'
$env:SOURCE_DATE_EPOCH = '1787356800'
$env:FORCE_SOURCE_DATE = '1'
$env:TZ = 'UTC'
New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null

Push-Location $sourceRoot
try {
    1..5 | ForEach-Object {
        & pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory $outputRoot EGA_FR.tex
        if ($LASTEXITCODE -ne 0) { throw "pdfLaTeX pass $_ failed with exit code $LASTEXITCODE" }
    }
} finally {
    Pop-Location
}

$pdf = Join-Path $outputRoot 'EGA_FR.pdf'
if (-not (Test-Path -LiteralPath $pdf)) { throw 'Expected French reader PDF was not produced.' }
Get-Item -LiteralPath $pdf | Select-Object FullName,Length
Get-FileHash -Algorithm SHA256 -LiteralPath $pdf
