var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var CopyWebpackPlugin = require('copy-webpack-plugin');


module.exports = {
    context: __dirname,
    entry: [
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        './assets/js/index'
    ],

    output: {
        path: path.resolve('./assets/bundles/'),
        filename: '[name]-[hash].js',
        publicPath: 'http://localhost:3000/assets/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
    },

    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack-stats.json'}),
        new CopyWebpackPlugin([
            { from: 'node_modules/flocs-visual-components/lib/static/images'
                , to: 'static/images'
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
            { test: /\.(png)$/,  loader: "url-loader?limit=8000" },
            { test: /\.woff|woff2$/,  loader: "url-loader?limit=10000&mimetype=application/font-woff" },
            { test: /\.ttf$/,    loader: "file-loader" },
            { test: /\.eot$/,    loader: "file-loader" },
            { test: /\.svg$/,    loader: "file-loader" }
        ]
    },

    resolve: {
        modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['', '.js', '.jsx'],
        alias:{
            images: path.resolve('./assets/images')
        }
    }
}
