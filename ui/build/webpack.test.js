const base = require('./webpack.base')
const nodeExternals = require('webpack-node-externals')

module.exports = {
  ...base,
  externals: [nodeExternals()],
  devtool: 'inline-cheap-module-source-map'
}
