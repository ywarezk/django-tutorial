/**
 * webpack configuration
 */

var path = require('path');
module.exports = {
    entry: './src/client.js',

    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, '../static/login_react/js/')
    },

    module: {
        loaders: [
            {test: /\.js$/, loader: 'babel-loader'}
        ]
    }

}