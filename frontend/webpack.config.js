var path = require("path")
var webpack = require('webpack')
var CopyWebpackPlugin = require('copy-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker');


module.exports = {
    context: __dirname,
    entry: [
        './js/index'
    ],

    output: {
        path: path.resolve('./static/'),
        filename: 'bundles/main.js',
        publicPath: '/static/'
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new CopyWebpackPlugin([
            { from: 'node_modules/flocs-visual-components/lib/static/images'
                , to: 'images'
            }
        ])
    ],

    module: {
        loaders: [
            // JSX
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loaders: ['babel']
            },

            // CSS
            {
                test: /\.css$/,
                loader: "style-loader!css-loader"
            },

            // Images
            { test: /\.(png)$/,  loader: "url-loader?limit=8000&name=/images/[name].[ext]" },
            { test: /\.woff|woff2$/,  loader: "url-loader?limit=10000&mimetype=application/font-woff&name=/fonts/[name].[ext]" },
            { test: /\.ttf|eot|svg$/,    loader: "file-loader" }
        ]
    },

    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx'],
        alias:{
            images: path.resolve('./images')
        }
    }
}