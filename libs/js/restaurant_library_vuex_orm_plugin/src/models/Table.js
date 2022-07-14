import { Model } from '@vuex-orm/core'
import Restaurant from './Restaurant'

export default class Table extends Model {
  static entity = 'Table'

  static jsonApiConfig = {
    entityToResourceRouteCase: x => "Tables"
  }

  static fields() {
    return {
      typeForSerialization: this.attr("Table"),

      id: this.attr(null),
      name: this.attr(''),

      restaurant_id: this.attr(null),
      restaurant: this.belongsTo(Restaurant, 'restaurant_id')   
    }
  }
}