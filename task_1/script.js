"use strict";
const yandexMap = (function() {
    var myMap = new Object();

    return {
        init: function() {
            ymaps.ready(createMap);

            function createMap() {
                myMap = new ymaps.Map("map", {
                    center: [55.76, 37.64],
                    zoom: 8,
                    controls: [
                        'zoomControl',
                        'rulerControl',
                        'typeSelector',
                        'fullscreenControl',
                    ]
                });

            };
        },
        get: function() {
            return myMap;
        },

    };
})();

const addressesOnMap = (function() {
    var myMap;
    var addresses_coord = {};

    function addAddressOnMap(find_geoobject) {
        var myGeocoder = ymaps.geocode(
            find_geoobject, {
                results: 1
            });
        myGeocoder.then(function(res) {
                var coordinates = res.geoObjects.get(0).geometry.getCoordinates();
                addresses_coord[find_geoobject] = coordinates;
                var placemark = new ymaps.Placemark(
                    coordinates, {
                        'hintContent': find_geoobject,
                        'balloonContent': find_geoobject,
                    }
                );
                myMap.geoObjects.add(placemark);

            },
            function(error) {
                alert("Возникла ошибка: " + error.message);
            }
        );
    };

    return {
        add: function(addr) {
            ymaps.ready(addAddressesOnMap(addr));

            function addAddressesOnMap(addr) {
                return function() {
                    myMap = yandexMap.get();
                    for (let i = 0; i < addr.length; i++) {
                        addAddressOnMap(addr[i]);
                    };
                };
            }
        },
        get: function() {
            return addresses_coord
        },
    };
})();


const addresses = (function() {
    var addr = [];
    return {
        init: function(spreadsheetdata) {
            var raw_addresses = (spreadsheetdata.feed.entry.map(function(cell) {
                return cell.content.$t
            }));
            var beginFromFirstAddress = 1
            addr = raw_addresses.slice(beginFromFirstAddress);
        },
        get: function() {
            return addr;
        },
        render: function() {
            var addr = addresses.get();
            var htmlAddresses = '';
            for (let i = 0; i < addr.length; i++) {
                htmlAddresses += '<p onclick=\"addresses.centerAddressOnMap(this)\">' + addr[i] + '</p>';
            }
            var container = document.getElementById('addresses_container');
            container.innerHTML = htmlAddresses;
        },
        centerAddressOnMap: function(e) {
            var addrToCenter = e.innerHTML;
            if (addressesOnMap.get()[addrToCenter] === undefined) {
                alert("Адрес '" + addrToCenter + "' не найден!");
            } else {
                yandexMap.get().setCenter(addressesOnMap.get()[addrToCenter]);
            };
        },
    };
})();
