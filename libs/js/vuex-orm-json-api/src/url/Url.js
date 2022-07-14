export default class {
  /**
   * Creates new url
   */

  constructor(endpoint, config) {
    this.endpoint = endpoint;
    this.config = config;
  }

  /**
   * Url start
   */
  stringify() {
    return this.endpoint + '/';
  }
}
