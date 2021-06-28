let apiKeyy = '1be9a6884abd4c3ea143b59ca317c6b2';

$.getJSON('https://ipgeolocation.abstractapi.com/v1/?api_key=' + apiKeyy, function(data) {
  console.log(JSON.stringify(data, null, 2));
});