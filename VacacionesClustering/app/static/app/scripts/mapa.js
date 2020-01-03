var colores = [];
var clusters;
// Se utilizara openstreet map
var osmUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
    osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    osm = L.tileLayer(osmUrl, {
        maxZoom: 18,
        attribution: osmAttrib
    });

// Se inicializa el mapa con Mexico como centro y un zoom de 5
var map = L.map('map').setView([19.3911668, -99.423815], 5).addLayer(osm), geocoder = L.Control.Geocoder.nominatim();

// Se maneja el doble click en el mapa
map.on('dblclick', onMapClick);

// Script for adding marker on map click
function onMapClick(e) {
    geocoder.reverse(e.latlng, map.options.crs.scale(map.getZoom()), function (results) {
        var r = results[0];
        var geojsonFeature = {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "type": "Point",
                "coordinates": [e.latlng.lat, e.latlng.lng]
            }
        };
        var marker;

        L.geoJson(geojsonFeature, {
            pointToLayer: function (feature, latlng) {
                marker = L.marker(e.latlng, {
                    title: r.name,
                    alt: r.name,
                    riseOnHover: true,
                    draggable: true
                }).bindPopup(String(r.html || r.name) +
                    "<br /><br /><center><input type='button' value='Eliminar sitio' class='marker-delete-button'/></center>");

                marker.on("popupopen", onPopupOpen);

                return marker;
            }
        }).addTo(map);
    });
}

// Maneja el popup del marcador
function onPopupOpen() {
    var tempMarker = this;
    $(".marker-delete-button:visible").click(function () {
        map.removeLayer(tempMarker);
    });
}

// Obtiene los marcadores
function getAllMarkers() {
    var allMarkersObjArray = [];
    var allMarkersGeoJsonArray = [];
    var content = [];
    clusters = $("#clusters").val();
    $.each(map._layers, function (ml) {
        if (map._layers[ml].feature) {
            var modelo = {
                "latitud": this.getLatLng().lat,
                "longitud": this.getLatLng().lng,
                "nombre": this["defaultOptions"].title,
                "clusters": clusters
            };
            content.push(modelo);
            allMarkersObjArray.push(this);
            allMarkersGeoJsonArray.push(JSON.stringify(this.toGeoJSON()));
        }
    });

    var features = [];
    map.eachLayer(function (layer) {
        if (layer instanceof L.Marker) {
            features.push(layer.feature);
        }
    });

    $.ajax({
        url: window.location.href + "api/lugares/",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        type: 'POST',
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
        },
        data: JSON.stringify(content),
        success: function (data) {
            for (i = 0; i < clusters; i++) {
                colores.push(colorAleatorio());
                $('#resultados').append('<li class="active"><a href="#cluster' + i +
                    '" data-toggle="collapse" aria-expanded="false">Dia ' +
                    (i + 1) + '</a><ul class="collapse list-unstyled" id="cluster' + i + '"></ul></li>');
            }
            quitaMarcadores();
            resultado = JSON.parse(data);
            $.each(resultado, function (index, value) {
                var agrupacion = resultado[index].Cluster;
                creaMarcador(resultado[index], agrupacion);
                $('#cluster' + agrupacion).append('<li>' + resultado[index].Nombre + '</li>')
            });
        },
        error: function (jqXHR, textStatus, errorThrown) {
            alert(JSON.stringify(jqXHR.responseJSON));
        }
    });
}

$(".get-markers").click(function (event) {
    event.preventDefault();
    if ($("#clusters").val()) {
        $('#resultados').html('');
        getAllMarkers();
    }
    else {
        alert("Ingrese el numero de clusters")
    }
});

function colorAleatorio() {
    var caracteres = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += caracteres[Math.floor(Math.random() * 16)];
    }
    return color;
}

function quitaMarcadores() {
    $.each(map._layers, function (ml) {
        if (map._layers[ml].feature) {
            map.removeLayer(this);
        }
    });
}

function creaMarcador(data, color) {
    var geojsonFeature = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Point",
            "coordinates": [data.Longitud, data.Latitud]
        }
    };
    var marker;
    var latlng = new L.latLng(data.Longitud, data.Latitud);

    L.geoJson(geojsonFeature, {
        pointToLayer: function (feature, latlng) {
            marker = L.marker(latlng, {
                title: data.Nombre,
                alt: data.Nombre,
                riseOnHover: true,
                draggable: false,
                icon: L.KNreiseMarkers.icon({ markerColor: colores[color] })
            }).bindPopup(String(data.Nombre) + "<br />Visitar el <span>" + String(data.DiadeVacaciones) +
                "</span><br /><br /><center><input type='button' value='Eliminar sitio' class='marker-delete-button'/></center>");

            marker.on("popupopen", onPopupOpen);

            return marker;
        }
    }).addTo(map);
}