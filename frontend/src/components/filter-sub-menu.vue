<template>
  <div>
    <v-slide-x-transition hide-on-leave>
      <v-list-item v-if="filterMode === 'base'" @click="setFilterMode(name)">
        <v-list-item-content>
          <v-list-item-title class="filterMenu">
            {{ capName }}
            <v-icon v-if="filter.length > 0" class="nameChevron">{{
              mdiChevronRightCircle
            }}</v-icon>
            <v-icon v-else class="nameChevron">{{ mdiChevronRight }}</v-icon>
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-slide-x-transition>
    <v-slide-x-reverse-transition hide-on-leave>
      <div v-if="filterMode === name">
        <header class="filterHeader">
          <v-list-item @click="setFilterMode('base')">
            <v-list-item-content>
              <v-list-item-title class="filterTitle"
                ><v-icon>{{ mdiChevronLeft }}</v-icon
                >{{ name }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-text-field
            v-model="query"
            placeholder="Filter"
            full-width
            dense
            filled
            rounded
            hide-details="auto"
          />
        </header>
        <v-list-item-group
          v-model="filter"
          class="filterGroup overflow-y-auto"
          multiple
        >
          <v-list-item
            v-for="item of choices"
            :key="name + ':' + item.value"
            :value="item.value"
            dense
            ripple
          >
            <v-list-item-content>
              <v-list-item-title>{{ item.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </div>
    </v-slide-x-reverse-transition>
  </div>
</template>

<script>
import {
  mdiChevronLeft,
  mdiChevronRight,
  mdiChevronRightCircle,
} from "@mdi/js";
import { mapState } from "vuex";

export default {
  name: "FilterSubMenu",
  props: {
    name: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      mdiChevronLeft,
      mdiChevronRight,
      mdiChevronRightCircle,
      query: "",
      capName: this.name.charAt(0).toUpperCase() + this.name.slice(1),
    };
  },
  computed: {
    ...mapState("browser", {
      choices: function (state) {
        const unfilteredChoices = state.formChoices[this.name];
        const filteredChoices = [];
        for (let choice of unfilteredChoices) {
          if (choice.text.includes(this.query)) {
            filteredChoices.push(choice);
          }
        }
        return filteredChoices;
      },
      formChoices: (state) => state.formChoices,
      filters: (state) => state.settings.filters,
      filterMode: (state) => state.filterMode,
    }),
    filter: {
      get() {
        return this.filters[this.name];
      },
      set(value) {
        if (value.includes(0)) {
          console.error(this.name, "filter =", value);
        }
        const data = {
          filters: { [this.name]: value },
        };
        this.$store.dispatch("browser/settingChanged", data);
        this.$emit("sub-menu-click");
      },
    },
  },
  methods: {
    setFilterMode(mode) {
      this.$store.dispatch("browser/setFilterMode", {
        group: this.$route.params.group,
        pk: this.$route.params.pk,
        mode,
      });
      this.query = "";
    },
  },
};
</script>

<style scoped lang="scss">
.filterMenu {
  line-height: 24px !important;
}
.nameChevron {
  float: right;
}
.filterTitle {
  font-variant: small-caps;
  color: gray;
  font-weight: bold;
  font-size: 1.6rem !important;
}
.filterHeader {
}
.filterGroup {
  max-height: 85vh; /* has to be less than the menu height */
}
</style>
