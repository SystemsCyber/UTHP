module.exports = (req, res) => {
    req.session.userId = null;
    res.redirect('/login');
}