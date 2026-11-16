# Sirve el libro compilado por HTTP local.
# Uso (desde la raíz del proyecto):
#   .\serve.ps1            -> http://localhost:8000
#   .\serve.ps1 -Port 9000 -> http://localhost:9000
#
# Es necesario servir por HTTP (y no abrir _build/html/index.html con file://)
# porque los simulacros interactivos usan módulos ES y fetch(), que el navegador
# bloquea cuando la página se abre directamente desde el disco.

param([int]$Port = 8000)

$root = Join-Path $PSScriptRoot "_build\html"

if (-not (Test-Path $root)) {
    Write-Error "No existe '$root'. Ejecuta primero: jupyter-book build ."
    exit 1
}

Write-Host ""
Write-Host "Libro disponible en: http://localhost:$Port" -ForegroundColor Green
Write-Host "Simulacros:          http://localhost:$Port/Clases/Simulacros/" -ForegroundColor Green
Write-Host "Detén el servidor con Ctrl+C." -ForegroundColor DarkGray
Write-Host ""

python -m http.server $Port --directory $root
