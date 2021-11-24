export default function request(path, method, data=false) {
  var root = 'http://localhost:8000/'
  var xhr = new XMLHttpRequest()
  xhr.open(method, root + path, false)
  xhr.setRequestHeader('Content-type', 'application/json');

  if (data) {xhr.send(JSON.stringify(data))}
  else      {xhr.send()}
  console.log(xhr.response)

  return JSON.parse(xhr.response)
}