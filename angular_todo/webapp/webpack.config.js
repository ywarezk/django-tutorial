/**
 * Created by PC on 01/06/2017.
 */

var path = require('path');
module.exports = {

    entry: './src/app.module.ts',
    devtool: 'sourcemap',

    output: {
        filename: 'app.js',
        path: path.join(__dirname, '../static/angular_todo/js')
    },

    resolve: {
        extensions: ['.ts', '.js']
    },

    module: {
        loaders: [
            {test: /\.ts$/, loader: 'ts-loader'}
        ]
    }

}