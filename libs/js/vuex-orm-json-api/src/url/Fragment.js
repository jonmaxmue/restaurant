export default class {
  /**
   * Creates new parameter with config as supermarket xD
   */
  constructor(Url) {
    this.Url = Url;
    this.config = Url.config;

  }

  /**
   * Parmeter start
   */
  stringify() {
    return this.Url.endpoint + '?';
  }

  add(urlState, next) {
    if (next) {
      if (urlState.split('?').length > 1) {
        return urlState + '&' + next;
      }
      return urlState + '?' + next;
    }
    return urlState;
  }
}
