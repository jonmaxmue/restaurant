  <template>
    <div>
      <b-container>
        <div id="intro" class="mt-7 mb-7">
            <Intro />
        </div>
      </b-container>
      <b-container>
        <div id="description" class="mt-7 mb-7">
            <Description />
        </div>
      </b-container>
      <b-container-fluid>
        <div id="projects" class="mt-7 mb-7">
          <Projects :projects="projects" />
        </div>
      </b-container-fluid>
      <b-container>
        <div id="reservation" class="mt-7 mb-7">
            <Reservation />
        </div>
      </b-container>
    </div>
</template>

<script>

export default {
    layout: "onepage",
    transition: "fade",
    data() {
        return {
            projects: [
                {
                    title: "Zusammen",
                    description: "Wenn Sie Pasta, Lammbratwürste und feine Saucen gern selber machen und Ihre Gäste mit edlen Gerichten beeindrucken wollen, sind Sie hier genau richtig. Entdecken Sie Gourmet-Rezepte mit Fleisch, Gemüse, Nudeln, Kartoffeln, Reis und für traumhafte Desserts.",
                    image: require("~/assets/images/p1.png")
                },
                {
                    title: "Genießen",
                    description: "Die Antwort ist einfach. Essen ist universell. Jeder muss essen. So einfach ist das. Daher sind die Leute immer auf der Suche nach leckerem, gesunden Essen, den besten Restaurants etc. Kein Wunder, dass jeder übers Essen spricht.",
                    image: require("~/assets/images/p2.png")
                },
                {
                    title: "Leben",
                    description: "Essen ist natürlich eine großartige Möglichkeit, Leute zu treffen und neue Freunde zu finden. Wenn Menschen zusammen essen, kann man sicher sein, dass die Gespräche über Essen, Restaurants und Rezepte endlos sein werden.",
                    image: require("~/assets/images/p3.png")
                }
            ]
        };
    },
    head() {
        // Set Meta Tags for this Page
    },
    async asyncData({ params }) {
        const slug = params.abs; // When calling /abc the slug will be "abc"
        return { slug };
    }
}
</script>

<style>
  .red {
    color: red;
  }
</style>