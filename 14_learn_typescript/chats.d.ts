export declare module "./chats.js" {
  function log(chats: Array<Chat>): void;
  type Chat = {
    time: string;
    message: string;
  }
  export const chats: Array<Chat>;
}
