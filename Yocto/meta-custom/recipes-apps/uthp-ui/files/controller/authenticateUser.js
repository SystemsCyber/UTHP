const { default: axios } = require("axios");

module.exports = async (req, res) => {
    const { username, password } = req.body;

    try {
        const response = await axios.post('http://localhost:5000/api/login', {
            username: username,
            password: password
        });

        // Check response status
        if (response.status === 200) {
            // Assuming the API sends back a token or user data
            // res.status(200).json({
            //     message: 'Authentication successful',
            //     data: response.data
            // });

            // Access the data from the response
            const { user_id, message } = response.data;
            
            // Check if userId exists in the response
            if (user_id) {
                console.log('Received userId:', user_id, response.data);
                req.session.userId = user_id;
                // Redirect to tools page
                res.redirect('/tools');
            }

            
        } else {
            const errorMessage = "Invalid username or password";
            res.redirect(`/login?error=${encodeURIComponent(errorMessage)}`);
        }
    } catch (error) {
        
        //res.render('login', {error: error.message});
        res.redirect(`/login?error=${encodeURIComponent(error.message)}`);
    }
}