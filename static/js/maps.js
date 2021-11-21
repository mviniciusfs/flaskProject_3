let map;

function initMap() {
  // fetch('/data')
  //   .then((response) => response.json())
  //   .then((ev) => {

  //     const obj = ev.map((value) => value);
  //     console.log(obj);
  //     var nome = obj.map((ev) => ev.nome);
  //     var contato = obj.map((ev) => ev.contato);
  //     var email = obj.map((ev) => ev.email);
  //     var latitude = obj.map((ev) => ev.latitude);
  //     var longitude = obj.map((ev) => ev.longitude);
  //     var placa = obj.map((ev) => ev.placa);

  //     console.log(nome);
  //     console.log(contato);
  //     console.log(email);
  //     console.log(latitude);
  //     console.log(longitude);
  //     console.log(placa);

  //     map = new google.maps.Map(document.getElementById("map"), {
  //       center: { lat: -20.1165, lng: -40.1812 },
  //       zoom: 8,
  //     });
  //   });

  const location = { lat: -20.1165, lng: -40.1812  };
  const placa = "BRA2E19"
  const contentString = `<div ><p>Placa:${placa}</p></div>`;

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: location,
  });
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
}
//  initMap();