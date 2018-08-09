const express = require('express');
const app = express();
const port = 8081;

app.use('/', express.static(__dirname + '/document_root'));
app.listen(port, () => {
    console.log('Server Starts - port:' + port);
})
