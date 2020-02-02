Quick demonstration that even though HttpPlatform module is [technically still recommended](https://docs.microsoft.com/en-us/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2019) for running python webapps under IIS, it is entirely possible to use the official replacement ASP.NET Core Module (and ASP.NET Core Module V2). To do this, you'll need to:

0. ensure that python 3.8, IIS, asp.net core hosting bundle and httpplatformhandler 1.2 are installed
1. create a python 3.8 venv someplace
2. install requirements.txt into that venv
3. update the path to python.exe according to location of venv in
    * `httpplatform/web.config`
    * `ancm/web.config`
    * `ancmv2/web.config` 
4. create new sites under IIS pointing @ the `httpplatform`, `ancm` and `ancmv2` folders