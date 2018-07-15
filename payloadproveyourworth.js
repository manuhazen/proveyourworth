const proveRequest = new XMLHttpRequest();
const url = 'http://www.proveyourworth.net/level3/activate?statefulhash=da4abc2ea32d46f63f73969684e831b4&username=Bytes';
proveRequest.open('GET', url, false);
proveRequest.send(null);
let headers = proveRequest.getAllResponseHeaders();
let provePayload = headers.match(/\bhttps?:\/\/\S+/gi);
window.open(provePayload[0]);