import InsertionStore from '../InsertionStore';
import Utils from '../Utils';

export default class {
  constructor(database, config) {
    this.database = database;
    this.resourceToEntityCase = config.resourceToEntityCase;

    console.log("FetchRelated", config);
    this.fetchRelated = "fetchRelated" in config ? config.fetchRelated : "";
  }

  async transform(data) {
    let insertionStore = new InsertionStore();
    let primaryData = data.data;

    if (primaryData instanceof Array) {
      for (let i = 0; i < primaryData.length; i++) {
        await this.transformResource(primaryData[i], insertionStore);
      }
    } else {
      this.transformResource(primaryData, insertionStore);
    }

    let includedData = data.included || [];
    for (let i = 0; i < includedData.length; i++) {
      await this.transformResource(includedData[i], insertionStore);
    }
    
    return insertionStore;
  }

  async transformResource(data, insertionStore) {
    // Convert JSON:API casing to Vuex ORM casing and look up the model.
    let type = this.resourceToEntityCase(data.type);
    let model = Utils.modelFor(this.database, type);
    let resourceId = data.id;
    let localKey = model.localKey();
    let record = insertionStore.fetchRecord(type, resourceId, localKey);

    model.jsonApiTransformer.transform(data, record, insertionStore);

    return await model.jsonApiTransformer.requestRelated.requestPaths(this.fetchRelated);
  }
}
