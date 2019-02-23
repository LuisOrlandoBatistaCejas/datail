# Datail apl

This project was is made with Django 2.1 and Angular version 7.3.1.


## Starting

Windows Run `venv\Scripts\activate.bat` to activate virtual-enviroment for python

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.
Run
`cd django-app
 python manage.py collectstatic
`
this way you collect all statics generated by the angular-app

## Request
 `[GET] BASE_URL/rest/comprobante` list all comprobantes
 `[POST] BASE_URL/rest/comprobante` create a comprobante with the request multipart
 `[PUT] BASE_URL/rest/comprobante/:id` update :id comprobante with the request multipart
 `[DELETE] BASE_URL/rest/comprobante/:id` drop :id comprobante with cascade to comprobante_deails

 `[GET] BASE_URL/rest/details` list all comprobantes_detalles
 `[GET] BASE_URL/rest/details/?ruc=:ruc&numero=:numero` list all 'comprobantes_detalles' related to a 'comprobante' with the given ':ruc' and the given ':numero'
 `[POST] BASE_URL/rest/details` create a comprobante_detalle with the request multipart
 `[PUT] BASE_URL/rest/details/:id` update :id comprobante_detalle with the request multipart
 `[DELETE] BASE_URL/rest/details/:id` drop :id comprobante with cascade to comprobante_deails