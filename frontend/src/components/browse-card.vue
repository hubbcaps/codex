<template>
  <div class="browsePaneWrapper">
    <v-lazy
      v-for="item in itemList"
      :key="item.pk"
      transition="scale-transition"
    >
      <div class="browseTile">
        <div class="browseTileContent">
          <div class="coverWrapper">
            <BookCover
              :cover-path="item.cover_path"
              :progress="+item.progress"
            />
            <div
              v-if="!item.finished"
              class="unreadFlag"
              :class="{ mixedreadFlag: item.finished === null }"
            />
            <div class="coverOverlay">
              <router-link class="browseLink" :to="getToRoute(item)">
                <div class="coverOverlayTopRow">
                  <span v-if="item.child_count" class="childCount">
                    {{ item.child_count }}
                  </span>
                </div>
                <div class="coverOverlayMiddleRow">
                  <v-icon v-if="item.group === 'c'">{{ mdiEye }}</v-icon>
                </div>
              </router-link>
              <div class="coverOverlayBottomRow">
                <MetadataButton
                  v-if="item.group === 'c'"
                  class="metadataButton"
                  :pk="item.pk"
                />
                <BrowseContainerMenu
                  :group="item.group"
                  :pk="item.pk"
                  :finished="item.finished"
                />
              </div>
            </div>
          </div>
          <router-link
            class="browseLink cardSubtitle text-caption"
            :to="getToRoute(item)"
          >
            <div class="headerName">
              {{ item.header_name }}
            </div>
            <div class="displayName">
              {{ item.display_name }}
            </div>
          </router-link>
        </div>
      </div>
    </v-lazy>
  </div>
</template>

<script>
// import { mdiChevronLeft } from "@mdi/js";
import { mdiDotsVertical, mdiEye } from "@mdi/js";
import { mapState } from "vuex";

import BookCover from "@/components/book-cover";
import BrowseContainerMenu from "@/components/browse-container-menu";
import MetadataButton from "@/components/metadata-dialog";
import { getReaderRoute } from "@/router/route";

export default {
  name: "BrowseCard",
  components: {
    BookCover,
    BrowseContainerMenu,
    MetadataButton,
  },
  props: {
    itemList: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      mdiDotsVertical,
      mdiEye,
    };
  },
  computed: {
    ...mapState("browser", {}),
  },
  methods: {
    getToRoute(item) {
      if (item.group === "c") {
        return getReaderRoute(item);
      } else {
        return { name: "browser", params: { group: item.group, pk: item.pk } };
      }
    },
    markRead: function (group, pk, finished) {
      this.$store.dispatch("browser/markRead", { group, pk, finished });
    },
  },
};
</script>

<style scoped lang="scss">
@import "~vuetify/src/styles/styles.sass";
.browseTile {
  float: left;
  padding: 16px;
  text-decoration: none;
  text-align: center;
}
.browseTileContent {
  height: 250px;
  width: 120px;
}
.coverWrapper {
  position: relative;
}
.coverOverlay {
  position: absolute;
  top: 0px;
  height: 100%;
  width: 100%;
  text-align: center;
  border-radius: 5px;
  border: solid thin transparent;
}
.coverWrapper:hover > .coverOverlay {
  background-color: rgba(0, 0, 0, 0.5);
  border: solid thin #cc7b19;
}
.coverOverlay > * {
  width: 100%;
}
.coverWrapper:hover > .coverOverlay * {
  /* optimize-css-assets-webpack-plugin / cssnano bug destroys % values. 
     use decimals instead.
     https://github.com/NMFR/optimize-css-assets-webpack-plugin/issues/118
  */
  opacity: 1;
}
.coverOverlayTopRow,
.coverOverlayBottomRow {
  height: 15%;
}
.coverOverlayTopRow {
  display: flex;
  opacity: 1;
}
.coverOverlayMiddleRow {
  height: 70%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.coverOverlayMiddleRow,
.coverOverlayBottomRow {
  opacity: 0;
}
.coverOverlayBottomRow {
  display: flex;
}
.childCount {
  position: absolute;
  top: 0;
  left: 0;
  display: inline;
  min-width: 1.5rem;
  padding: 0rem 0.25rem 0rem 0.25rem;
  border-radius: 50%;
  background-color: black;
  color: white;
  opacity: 0.75;
}
.unreadFlag {
  position: absolute;
  top: 0;
  right: 0;
  display: block;
  width: 24px;
  height: 24px;
  background: linear-gradient(
    45deg,
    transparent 50%,
    rgba(0, 0, 0, 0.5) 60%,
    var(--v-primary-base) 60%
  );
  border-radius: 5px;
}
.mixedreadFlag {
  background: linear-gradient(
    45deg,
    transparent 50%,
    rgba(0, 0, 0, 0.5) 60%,
    var(--v-primary-base) 60%,
    var(--v-primary-base) 70%,
    transparent 70%,
    rgba(0, 0, 0, 0.5) 80%,
    var(--v-primary-base) 80%,
    var(--v-primary-base) 90%,
    transparent 90%
  );
}
.metadataButton {
  position: absolute;
  bottom: 3px;
  left: 3px;
}
.browseLink {
  text-decoration: none;
  color: inherit;
}
.cardSubtitle {
  margin-top: 7px;
  padding-top: 3px;
}
.headerName {
  padding-top: 5px;
  color: gray;
}
@media #{map-get($display-breakpoints, 'sm-and-down')} {
  .browseTile {
    padding: 8px;
  }
  .browseTileContent {
    width: 100px;
  }
}
</style>
