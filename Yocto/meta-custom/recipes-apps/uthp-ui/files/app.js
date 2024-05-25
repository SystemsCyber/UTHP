const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();

// Controllers
const homePageController = require('./controller/homePage');
const authenticateUserController = require('./controller/authenticateUser');
const loginPageController = require('./controller/loginPage');
const aboutPageController = require('./controller/aboutPage');
const toolPageControllers = require('./controller/toolsPage');
const logoutController = require('./controller/logout');

const expressSession = require('express-session');

// Serve static files from the public directory
app.use(express.static('public'));

// Edge template staff
app.use(require('express-edge'));
app.set('views', path.join(__dirname, 'views'));

// Body Parser JSON
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

// express session
app.use(expressSession({
    secret: 'your_secret_key',  // Replace with a secure key
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }  // Set secure: true if using HTTPS
}));

// Middleware to pass session data to views
app.use((req, res, next) => {
    res.locals.userId = req.session.userId;  // Make user_id available to all views
    next();
  });
  
// Route 
app.get('/', homePageController);
app.get('/login', loginPageController); // Diaplay login Page
app.post('/login', authenticateUserController); // Authenticate user
app.get('/about', aboutPageController); // About Route
app.get('/tools', toolPageControllers); // Tools demo for UTHP
app.get('/logout', logoutController); // Logout handler

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
