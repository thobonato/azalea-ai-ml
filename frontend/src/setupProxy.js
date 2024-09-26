const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'https://azalea-ai-ml-4959da38218c.herokuapp.com',
      // target: 'http://localhost:8000',
      changeOrigin: true,
      withCredentials: true,
      pathRewrite: {
        '^/api': '/api'
      }
    })
  );
};