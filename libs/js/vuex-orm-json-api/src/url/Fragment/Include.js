import Fragment from '.';

export default class extends Fragment {
  /**
   * Creates a new include with an array of strings
   */
  constructor(Url) {
    super(Url);


    if ('include' in this.config) {
      this.include =  this.config.include;
    }
    else {
      this.include = [];
    }
  }

  /**
   * Build jsonApi include
   */
  stringify() {
    let include = '';
    if (this.include.length) {
      include  = 'include=' + this.include.join(',');
    }
    return this.add(this.Url.stringify(), include);
  }
}
