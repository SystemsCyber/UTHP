module.exports = (req, res) => {
    // const error = req.session.errorMessage;
    // req.session.errorMessage = null; // Clear the message after displaying it
    
    res.render('login', {
        error: decodeURIComponent(req.query.error || '')
    });
}