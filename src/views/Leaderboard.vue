<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-simple-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Points</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in items" :key="item.name">
                <td>{{ item.name }}</td>
                <td>{{ item.points }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { name: 'John Doe', points: 234 },
        { name: 'Max Mustermann', points: 575 },
        { name: 'Carl Due', points: 2323 },
        { name: 'Kerstin Schuster', points: 5754 },
        { name: 'Alex Schmidt', points: 1004 },
        { name: 'Patrick Stolz', points: 899 }
      ]
    }
  },
  mounted() {
    this.items.sort((a,b) => b.points - a.points)
  }
};
</script>

<style>
</style>