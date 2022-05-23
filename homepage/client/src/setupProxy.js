const { createProxyMiddleware } = require('http-proxy-middleware');
module.exports = function(app) {
    app.use(createProxyMiddleware ('...', 
    { target: 'http://localhost:5000',secure: false,
    changeOrigin: true }
)
);
app.use(createProxyMiddleware ('/test', 
{ target: 'http://127.0.0.1:8000/',
secure: false,
changeOrigin: false }
)
);

}

//remember to use export FLASK_RUN_PORT=8000 before typing flask run