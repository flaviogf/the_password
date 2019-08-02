const webpack = require('webpack')
const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = {
    entry: path.join(__dirname, 'static', 'src', 'index.js'),
    output: {
        path: path.join(__dirname, 'app', 'static'),
        filename: 'app.min.js'
    },
    optimization: {
        minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].css',
            chunkFilename: '[id].css',
        })
    ],
    module: {
        rules: [{
            test: /\.s?[ac]ss$/,
            loaders: [
                MiniCssExtractPlugin.loader,
                'css-loader',
                'sass-loader'
            ],
        }]
    }
}