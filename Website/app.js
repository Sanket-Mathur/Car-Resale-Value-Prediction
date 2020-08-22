const express = require('express');
const bodyParser = require('body-parser');

const spawn = require('child_process').spawn;

const app = express();

var urlencodedParser = bodyParser.urlencoded({ extended: false });

// public folder for static files like stylesheets and images
app.use(express.static('public'));

// Entry Points / Routes
app.get('/', (req, res) => {
	res.render('index.ejs', {data: ''});
});
app.post('/', urlencodedParser, (req, res) => {
	var details = [req.body.price, req.body.kms, req.body.fuel, req.body.seller, req.body.trans, req.body.own, req.body.age];
	// Predicting the value by running script.py
	var script = spawn('python3', ["script.py", details])
	script.stdout.on('data', function(data) {
		res.render('index.ejs', {data: data});
	});	
});

// Port Number
app.listen(3000);
