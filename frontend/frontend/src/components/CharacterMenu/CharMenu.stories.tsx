import CharMenu from "./CharMenu";
import { ComponentMeta, ComponentStory } from "@storybook/react";
import React from "react";
import { withRouter } from "storybook-addon-react-router-v6";

// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
  title: "Menus/CharMenu",
  decorators: [withRouter],
  component: CharMenu,
  parameters: {
    layout: "padded",
  },

  // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
} as ComponentMeta<typeof CharMenu>;

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template: ComponentStory<typeof CharMenu> = (args) => <CharMenu {...args} />;

export const Primary = Template.bind({});

Primary.args = {
  isLoading: false,
  error: false,
  data: [
    {
      name: "Link Cat 1",
      links: [
        {
          name: "Link Item 1",
          link: "/link/item/1",
        },
        {
          name: "Link Item 2",
          link: "/link/item/2",
        },
      ],
    },
  ],
  characterID: "1",
};
