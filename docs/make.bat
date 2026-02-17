@ECHO OFF

set SPHINXBUILD=sphinx-build
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help
if "%1" == "help" goto help
if "%1" == "clean" goto clean

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR%
GOTO end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR%
GOTO end

:clean
rmdir /S /Q %BUILDDIR%
GOTO end

:end
