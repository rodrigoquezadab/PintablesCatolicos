@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Actualizando la biblioteca de Pintables Catolicos...
echo.
where python >nul 2>nul
if %errorlevel%==0 (
  python actualizar_biblioteca.py
) else (
  py actualizar_biblioteca.py
)
echo.
echo Listo. Vuelve a la aplicacion y pulsa "Actualizar" (o recarga la pagina).
pause
