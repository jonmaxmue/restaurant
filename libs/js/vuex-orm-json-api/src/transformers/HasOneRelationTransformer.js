import RelationTransformer from './RelationTransformer';

export default class extends RelationTransformer {
  transform(data, output, selfId = null, insertionStore = null) {
    /*
     * `null` is an acceptable value for to-one relationships: See
     * `https://jsonapi.org/format/#document-resource-object-linkage`.
     */
    if (data === null) {
      return null;
    }

    this.constructor.checkSingleton(data);

    let relatedModel = this.relation.related;
    let relatedLocalKey = relatedModel.localKey();
    let {type: resourceType, id} = data;

    /*
     * See `https://vuex-orm.org/guide/model/relationships.html#one-to-one`,
     * `https://vuex-orm.org/guide/model/relationships.html#one-to-one-inverse`, and
     * `https://vuex-orm.org/guide/model/relationships.html#one-to-one-polymorphic`.
     */

    let type = this.resourceToEntityCase(resourceType);

    this.constructor.checkType(type, relatedModel);

    if (insertionStore) {
      /*
       * Instead of creating an embedded record, defer to the `InsertionStore` and make this record visible to later
       * JSON:API resources.
       */
      let record = insertionStore.fetchRecord(type, id, relatedLocalKey);

      // Fill in the inverse side of this relation.
      if (!this.isPolymorphic) {
        record[this.relation.foreignKey] = selfId;
      } else {
        record[this.relation.id] = selfId;
        record[this.relation.type] = this.relation.model.entity;
      }
    } else {
      output[this.name] = {[relatedLocalKey]: id};
    }

    return output;
  }
}
