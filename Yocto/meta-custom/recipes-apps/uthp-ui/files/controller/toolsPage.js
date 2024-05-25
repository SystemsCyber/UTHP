module.exports = (req, res) => {
    console.log(req.session);
    if(req.session.userId) {
        return res.render('tools');
    }

    res.redirect('/login')
}