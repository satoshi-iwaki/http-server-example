const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('crypto');
const app = express();
const port = 8081;
const shasum = crypto.createHash('sha256');

app.use(bodyParser.text());
app.post('/api/digest', (req, res) => {
	shasum.update(req.body);
	const digest = shasum.digest('hex');
	const body = JSON.stringify({
		content: req.body,
		digest: digest.toString()
	});
	res.append('Content-Type', 'application/json');
	res.send(body);
});
app.listen(port, () => {
	console.log('Server Starts - port:' + port);
});
