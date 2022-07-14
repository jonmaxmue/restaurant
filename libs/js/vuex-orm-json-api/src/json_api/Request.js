import Utils from '../Utils';
import Response from './Response';
import Filter from '../url/Fragment/Filter';
import Include from '../url/Fragment/Include';
import Url from '../url/Url';
var JSONAPISerializer = require('jsonapi-serializer').Serializer;

export default class {
  /**
   * Creates a new request.
   */
  constructor(model) {
    this.model = model;
  }

  /*
   * Gets the axios instance.
   */
  get axios() {
    if (!this.model.axios) {
      return Utils.error('The axios instance is not registered. Please register the axios instance to the model.');
    }
    return this.model.axios;
  }

  /**
   * Performs an HTTP `GET`.
   */
  get(url, config = {}, map=true) {
    url = new Include(new Filter(new Url(url, config))).stringify();
    console.log(url, config);
    return this.request({
      ...this.model.globalJsonApiConfig,
      ...this.model.jsonApiConfig,
      method: 'get', url,
      ...config,
    }, map);
  }

  /**
   * Performs an HTTP `POST`.
   */
  post(url, data = {}, config = {}, map=true) {
    url = new Url(url, config).stringify();
    return this.request({
      ...this.model.globalJsonApiConfig,
      ...this.model.jsonApiConfig,
      method: 'post', url, data,
      ...config,

    }, map);
  }

  /**
   * Performs an HTTP `PUT`.
   */
  put(url, data = {}, config = {}, map=true) {
    url = new Url(url, config).stringify();

    return this.request({
      ...this.model.globalJsonApiConfig,
      ...this.model.jsonApiConfig,
      method: 'put', url, data,
      ...config,
    }, map);
  }

  /**
   * Performs an HTTP `PATCH`.
   */
  patch(url, data = {}, config = {}, map=true) {
    url = new Url(url, config).stringify();

    return this.request({
      ...this.model.globalJsonApiConfig,
      ...this.model.jsonApiConfig,
      method: 'patch', url, data,
      ...config,
    }, map);
  }

  /**
   * Performs an HTTP `DELETE`.
   */
  delete(url, config = {}, map=true) {
    url = new Url(url, config).stringify();
    
    return this.request({
      ...this.model.globalJsonApiConfig,
      ...this.model.jsonApiConfig,
      method: 'delete', url,
      ...config,
    }, map);
  }

  /**
   * Performs data serialization
   */
  serialize(data = {}) {

    var itemProperties = item => {
      return {ref: 'id',
        typeForAttribute: function (attribute, data) {
          return data.typeForSerialization;
        },
        attributes: Object.keys(item),
        keyForAttribute: 'underscore_case',
        pluralizeType: false,
        nullIfMissing: true,
        transform: function (record) {
        // Remove null attributes
          return Object.entries(record).reduce((a, [k, v]) => (v === null ? a : (a[k]=v, a)), {});
        }};
    };

    var options = itemProperties(data);
    // only for two dimensions of items serialization
    for (const [key, value] of Object.entries(data)) {
      if (value && typeof value === 'object' && 'typeForSerialization' in value) {
        options[key] = itemProperties(value);
      }
    }
    return new JSONAPISerializer(this.model.entity, options).serialize(data);
  }

  /**
   * Performs an API request: Awaits an axios request, gets the axios response, and awaits the database commit.
   */
  async request(config, map) {
    if (map) {
      return await new Response(this.model, await this.axios.request(config), config).commit();
    }
    return await this.axios.request(config);
  }
}
