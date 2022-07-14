import Fragment from '.';

export default class extends Fragment {
  /**
   * Creates a new filter
   */
  constructor(Url) {
    super(Url);

    if ('filter' in this.config) {
      this.filter =  this.config.filter;
    }
    else {
      this.filter = {};
    }
  }

  stringify() {
    let filter = '';
    for (const [key, value] of Object.entries(this.filter)) {
      filter += `filter[${key}]=${value}&`;
    }
    filter = filter.slice(0, -1);
    return this.add(this.Url.stringify(), filter);
  }
}
