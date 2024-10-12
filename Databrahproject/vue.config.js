module.exports = {
  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'assets',
  lintOnSave: true,  // Automatische Linter-Fehler anzeigen
  devServer: {
    port: 8080,  // Legt den Entwicklungsserver-Port fest
    open: true,  // Öffnet den Browser automatisch
  }
};
