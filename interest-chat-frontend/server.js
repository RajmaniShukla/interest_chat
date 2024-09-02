const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');

// Routes
app.get('/', (req, res) => {
    res.render('index');
});

app.post('/register', async (req, res) => {
    const { username, email,password } = req.body;
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/register/', { username, email, password });
        res.send(response.data);
    } catch (error) {
        res.status(500).send('Error registering user');
    }
});

app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', { username, password });
        //res.send(response.data);
        const data = response.data;
        res.render('dashboard',{ data });
    } catch (error) {
        console.error(error);
        res.status(500).send('Error logging in');
    }
});

app.post('/interest', async (req, res) => {
    const { username, interest } = req.body;
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/interest/', { username, interest });
        res.send(response.data);
    } catch (error) {
        res.status(500).send('Error saving interest');
    }
});

app.post('/message', async (req, res) => {
    const { from, to, message } = req.body;
    try {
        const response = await axios.post('http://127.0.0.1:8000/api/message/', { from, to, message });
        res.send(response.data);
    } catch (error) {
        res.status(500).send('Error sending message');
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
