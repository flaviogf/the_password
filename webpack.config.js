const path = require('path')

const webpack = require('webpack')

module.exports = {
    entry: path.join(__dirname, 'static', 'src', 'index.js'),
    output: {
        path: path.join(__dirname, 'app', 'static'),
        filename: 'app.min.js'
    },
    module: {
        rules: [{
            test: /\.s?[ac]ss$/,
            loaders: [
                'style-loader',
                'css-loader',
                'sass-loader'
            ],
        }]
    }
}