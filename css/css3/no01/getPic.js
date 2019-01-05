const https = require('https')
const fs = require('fs')
const path = require('path')
let url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1546453371728&di=2ff03808f7da8a8f0305ccd4d433f348&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201601%2F22%2F20160122120359_tQHx4.thumb.700_0.jpeg'

https.get(url, (res) => {
  res.setEncoding('binary')
  let imgData = ''
  res.on('data', (chunk) => {
    imgData += chunk
  })
  res.on('end', () => {
    fs.writeFile(path.join(__dirname, 'kumonom.jpeg'), imgData, 'binary', (err) => {
      if (!err) {
        console.log('success')
      }
    })
  })
})
