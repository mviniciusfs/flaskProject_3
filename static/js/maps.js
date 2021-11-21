let map;
let markersArray;

function initMap() {

  fetch('/data')
    .then((response) => response.json())
    .then((ev) => {

      const obj = ev.map((value) => value);
      markersArray = obj
      // var nome = obj.map((ev) => ev.nome);
      // var contato = obj.map((ev) => ev.contato);
      // var email = obj.map((ev) => ev.email);
      // var latitude = obj.map((ev) => ev.latitude);
      // var longitude = obj.map((ev) => ev.longitude);
      // var placa = obj.map((ev) => ev.placa);

      // console.log(nome);
      // console.log(contato);
      // console.log(email);
      // console.log(latitude);
      // console.log(longitude);
      // console.log(placa);

      const location = { lat: -20.1165, lng: -40.1812 };
      const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: location,
      });
    });
}

function procurarPlaca() {
  var codigoPlaca = document.getElementById('codigoPlaca').value;
  var dadosPlaca = markersArray.filter(obj => {
    return obj.placa === codigoPlaca
  })
  if (dadosPlaca.length > 0) {
    const location = { lat: parseFloat(dadosPlaca[0].latitude), lng: parseFloat(dadosPlaca[0].longitude)};
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 16,
      center: location,
    });
    const contentString = `<div><br><p><b>Placa</b>: ${dadosPlaca[0].placa}</p></div>`;
    const infowindow = new google.maps.InfoWindow({
      content: contentString,
    });
    const marker = new google.maps.Marker({
      position: location,
      map,
      title: "Localização da placa",
    });
    marker.addListener("click", () => {
      infowindow.open({
        anchor: marker,
        map,
        shouldFocus: false,
      });
    });

    document.getElementById('nome').innerHTML = `Nome: ${dadosPlaca[0].nome}` ;
    document.getElementById('email').innerHTML = `E-mail: ${dadosPlaca[0].email}`;
    document.getElementById('contato').innerHTML = `contato: ${dadosPlaca[0].contato}`;

  }
}
