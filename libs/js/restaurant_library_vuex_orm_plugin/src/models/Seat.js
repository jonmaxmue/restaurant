import { Model } from '@vuex-orm/core'
import Table from './Table'

export default class Seat extends Model {
  static entity = 'Seat'

  static jsonApiConfig = {
    entityToResourceRouteCase: x => "Seats"
  }

  static fields() {
    return {
      typeForSerialization: this.attr("Seat"),

      id: this.attr(null),
      name: this.attr(''),

      table_id: this.attr(null),
      table: this.belongsTo(Table, 'table_id')   
    }
  }
}