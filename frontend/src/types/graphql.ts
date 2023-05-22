export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = {
    [K in keyof T]: T[K];
};
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & {
    [SubKey in K]?: Maybe<T[SubKey]>;
};
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & {
    [SubKey in K]: Maybe<T[SubKey]>;
};
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
    ID: string;
    String: string;
    Boolean: boolean;
    Int: number;
    Float: number;
    DateTime: any;
    ExpectedErrorType: any;
    GenericScalar: any;
    UUID: any;
    Upload: any;
};

export type CreateMeetingInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    meeting: CreateMeetingInputField;
};

export type CreateMeetingInputField = {
    fileBin?: InputMaybe<Scalars['Upload']>;
};

export type CreateMeetingPayload = {
    __typename?: 'CreateMeetingPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    meeting?: Maybe<MeetingNode>;
    success?: Maybe<Scalars['Boolean']>;
};

export type CreateTopicInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    topic: CreateTopicInputField;
};

export type CreateTopicInputField = {
    name: Scalars['String'];
};

export type CreateTopicPayload = {
    __typename?: 'CreateTopicPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type DeleteMeetingInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    id: Scalars['ID'];
};

export type DeleteMeetingPayload = {
    __typename?: 'DeleteMeetingPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type DeleteTopicInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    id: Scalars['ID'];
};

export type DeleteTopicPayload = {
    __typename?: 'DeleteTopicPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type MeetingNode = Node & {
    __typename?: 'MeetingNode';
    createdAt: Scalars['DateTime'];
    date?: Maybe<Scalars['DateTime']>;
    fileBin?: Maybe<Scalars['String']>;
    fileHash: Scalars['String'];
    filename?: Maybe<Scalars['String']>;
    /** The ID of the object */
    id: Scalars['ID'];
    jsonSummary?: Maybe<Scalars['GenericScalar']>;
    mimeType: Scalars['String'];
    processed?: Maybe<Scalars['Boolean']>;
    processedTaskId: Scalars['String'];
    processingCompleted?: Maybe<Scalars['Boolean']>;
    /** Size of this file in bytes */
    size?: Maybe<Scalars['Int']>;
    summarizationCompleted?: Maybe<Scalars['Boolean']>;
    summarized?: Maybe<Scalars['Boolean']>;
    summarizedTaskId: Scalars['String'];
    summary?: Maybe<Scalars['String']>;
    title?: Maybe<Scalars['String']>;
    topicSet: TopicNodeConnection;
    topics?: Maybe<Scalars['String']>;
    uid: Scalars['UUID'];
    updatedAt?: Maybe<Scalars['DateTime']>;
    uploadedByUser?: Maybe<UserNode>;
};

export type MeetingNodeTopicSetArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    last?: InputMaybe<Scalars['Int']>;
    name?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
};

export type MeetingNodeConnection = {
    __typename?: 'MeetingNodeConnection';
    /** Contains the nodes in this connection. */
    edges: Array<Maybe<MeetingNodeEdge>>;
    /** Pagination data for this connection. */
    pageInfo: PageInfo;
};

/** A Relay edge containing a `MeetingNode` and its cursor. */
export type MeetingNodeEdge = {
    __typename?: 'MeetingNodeEdge';
    /** A cursor for use in pagination */
    cursor: Scalars['String'];
    /** The item at the end of the edge */
    node?: Maybe<MeetingNode>;
};

export type Mutatation = {
    __typename?: 'Mutatation';
    createMeeting?: Maybe<CreateMeetingPayload>;
    createTopic?: Maybe<CreateTopicPayload>;
    deleteMeeting?: Maybe<DeleteMeetingPayload>;
    deleteTopic?: Maybe<DeleteTopicPayload>;
    resendActivationEmail?: Maybe<ResendActivationEmailPayload>;
    sendPasswordResetEmail?: Maybe<SendPasswordResetEmailPayload>;
    signin?: Maybe<SignInPayload>;
    signup?: Maybe<SignupPayload>;
    updateAccount?: Maybe<UpdateAccountPayload>;
    updateMeeting?: Maybe<UpdateMeetingPayload>;
    updateTopic?: Maybe<UpdateTopicPayload>;
    verifyAccount?: Maybe<VerifyAccountPayload>;
};

export type MutatationCreateMeetingArgs = {
    input: CreateMeetingInput;
};

export type MutatationCreateTopicArgs = {
    input: CreateTopicInput;
};

export type MutatationDeleteMeetingArgs = {
    input: DeleteMeetingInput;
};

export type MutatationDeleteTopicArgs = {
    input: DeleteTopicInput;
};

export type MutatationResendActivationEmailArgs = {
    input: ResendActivationEmailInput;
};

export type MutatationSendPasswordResetEmailArgs = {
    input: SendPasswordResetEmailInput;
};

export type MutatationSigninArgs = {
    input: SignInInput;
};

export type MutatationSignupArgs = {
    input: SignupInput;
};

export type MutatationUpdateAccountArgs = {
    input: UpdateAccountInput;
};

export type MutatationUpdateMeetingArgs = {
    input: UpdateMeetingInput;
};

export type MutatationUpdateTopicArgs = {
    input: UpdateTopicInput;
};

export type MutatationVerifyAccountArgs = {
    input: VerifyAccountInput;
};

/** An object with an ID */
export type Node = {
    /** The ID of the object */
    id: Scalars['ID'];
};

/** The Relay compliant `PageInfo` type, containing data necessary to paginate this connection. */
export type PageInfo = {
    __typename?: 'PageInfo';
    /** When paginating forwards, the cursor to continue. */
    endCursor?: Maybe<Scalars['String']>;
    /** When paginating forwards, are there more items? */
    hasNextPage: Scalars['Boolean'];
    /** When paginating backwards, are there more items? */
    hasPreviousPage: Scalars['Boolean'];
    /** When paginating backwards, the cursor to continue. */
    startCursor?: Maybe<Scalars['String']>;
};

export type Query = {
    __typename?: 'Query';
    Meeting?: Maybe<MeetingNode>;
    Meetings?: Maybe<MeetingNodeConnection>;
    me?: Maybe<UserNode>;
    topic?: Maybe<TopicNode>;
    topicEvents?: Maybe<Scalars['String']>;
    topics?: Maybe<TopicNodeConnection>;
    user?: Maybe<UserNode>;
    users?: Maybe<UserNodeConnection>;
};

export type QueryMeetingArgs = {
    id?: InputMaybe<Scalars['ID']>;
};

export type QueryMeetingsArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    createdAt?: InputMaybe<Scalars['DateTime']>;
    date?: InputMaybe<Scalars['DateTime']>;
    fileHash?: InputMaybe<Scalars['String']>;
    filename?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    last?: InputMaybe<Scalars['Int']>;
    mimeType?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
    processed?: InputMaybe<Scalars['Boolean']>;
    processedTaskId?: InputMaybe<Scalars['String']>;
    processingCompleted?: InputMaybe<Scalars['Boolean']>;
    size?: InputMaybe<Scalars['Int']>;
    summarizationCompleted?: InputMaybe<Scalars['Boolean']>;
    summarized?: InputMaybe<Scalars['Boolean']>;
    summarizedTaskId?: InputMaybe<Scalars['String']>;
    summary?: InputMaybe<Scalars['String']>;
    title?: InputMaybe<Scalars['String']>;
    topics?: InputMaybe<Scalars['String']>;
    uid?: InputMaybe<Scalars['UUID']>;
    updatedAt?: InputMaybe<Scalars['DateTime']>;
    uploadedByUser?: InputMaybe<Scalars['ID']>;
};

export type QueryTopicArgs = {
    id: Scalars['ID'];
};

export type QueryTopicEventsArgs = {
    name?: InputMaybe<Scalars['String']>;
};

export type QueryTopicsArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    last?: InputMaybe<Scalars['Int']>;
    name?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
};

export type QueryUserArgs = {
    id: Scalars['ID'];
};

export type QueryUsersArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    createdAt?: InputMaybe<Scalars['DateTime']>;
    dateJoined?: InputMaybe<Scalars['DateTime']>;
    email?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    firstName?: InputMaybe<Scalars['String']>;
    groups?: InputMaybe<Array<InputMaybe<Scalars['ID']>>>;
    isActive?: InputMaybe<Scalars['Boolean']>;
    isStaff?: InputMaybe<Scalars['Boolean']>;
    isSuperuser?: InputMaybe<Scalars['Boolean']>;
    last?: InputMaybe<Scalars['Int']>;
    lastLogin?: InputMaybe<Scalars['DateTime']>;
    lastName?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
    password?: InputMaybe<Scalars['String']>;
    uid?: InputMaybe<Scalars['UUID']>;
    updatedAt?: InputMaybe<Scalars['DateTime']>;
    userPermissions?: InputMaybe<Array<InputMaybe<Scalars['ID']>>>;
};

export type ResendActivationEmailInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    email: Scalars['String'];
};

export type ResendActivationEmailPayload = {
    __typename?: 'ResendActivationEmailPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type SendPasswordResetEmailInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    email: Scalars['String'];
};

export type SendPasswordResetEmailPayload = {
    __typename?: 'SendPasswordResetEmailPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type SignInInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    email: Scalars['String'];
    password: Scalars['String'];
};

export type SignInPayload = {
    __typename?: 'SignInPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
    token?: Maybe<Scalars['String']>;
};

export type SignupInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    email: Scalars['String'];
    password1: Scalars['String'];
    password2: Scalars['String'];
};

export type SignupPayload = {
    __typename?: 'SignupPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type Subscription = {
    __typename?: 'Subscription';
    test?: Maybe<Scalars['String']>;
    test1?: Maybe<Scalars['String']>;
    topicEvents?: Maybe<Scalars['String']>;
};

export type SubscriptionTopicEventsArgs = {
    id?: InputMaybe<Scalars['String']>;
};

export type TopicNode = Node & {
    __typename?: 'TopicNode';
    /** About topic */
    about?: Maybe<Scalars['String']>;
    createdAt?: Maybe<Scalars['DateTime']>;
    /** The ID of the object */
    id: Scalars['ID'];
    /** Maturity of topic */
    maturity?: Maybe<Scalars['Int']>;
    meetings: MeetingNodeConnection;
    /** Topic name */
    name?: Maybe<Scalars['String']>;
    /** Sub topics */
    subTopics: TopicNodeConnection;
    uid: Scalars['UUID'];
    updatedAt?: Maybe<Scalars['DateTime']>;
};

export type TopicNodeMeetingsArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    createdAt?: InputMaybe<Scalars['DateTime']>;
    date?: InputMaybe<Scalars['DateTime']>;
    fileHash?: InputMaybe<Scalars['String']>;
    filename?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    last?: InputMaybe<Scalars['Int']>;
    mimeType?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
    processed?: InputMaybe<Scalars['Boolean']>;
    processedTaskId?: InputMaybe<Scalars['String']>;
    processingCompleted?: InputMaybe<Scalars['Boolean']>;
    size?: InputMaybe<Scalars['Int']>;
    summarizationCompleted?: InputMaybe<Scalars['Boolean']>;
    summarized?: InputMaybe<Scalars['Boolean']>;
    summarizedTaskId?: InputMaybe<Scalars['String']>;
    summary?: InputMaybe<Scalars['String']>;
    title?: InputMaybe<Scalars['String']>;
    topics?: InputMaybe<Scalars['String']>;
    uid?: InputMaybe<Scalars['UUID']>;
    updatedAt?: InputMaybe<Scalars['DateTime']>;
    uploadedByUser?: InputMaybe<Scalars['ID']>;
};

export type TopicNodeSubTopicsArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    last?: InputMaybe<Scalars['Int']>;
    name?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
};

export type TopicNodeConnection = {
    __typename?: 'TopicNodeConnection';
    /** Contains the nodes in this connection. */
    edges: Array<Maybe<TopicNodeEdge>>;
    /** Pagination data for this connection. */
    pageInfo: PageInfo;
};

/** A Relay edge containing a `TopicNode` and its cursor. */
export type TopicNodeEdge = {
    __typename?: 'TopicNodeEdge';
    /** A cursor for use in pagination */
    cursor: Scalars['String'];
    /** The item at the end of the edge */
    node?: Maybe<TopicNode>;
};

export type UpdateAccountInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    email?: InputMaybe<Scalars['String']>;
    firstName?: InputMaybe<Scalars['String']>;
    lastName?: InputMaybe<Scalars['String']>;
};

export type UpdateAccountPayload = {
    __typename?: 'UpdateAccountPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type UpdateMeetingInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    meeting: UpdateMeetingInputField;
};

export type UpdateMeetingInputField = {
    date: Scalars['String'];
    id: Scalars['ID'];
    title: Scalars['String'];
};

export type UpdateMeetingPayload = {
    __typename?: 'UpdateMeetingPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type UpdateTopicInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    topic: UpdateTopicInputField;
};

export type UpdateTopicInputField = {
    id: Scalars['ID'];
    name: Scalars['String'];
};

export type UpdateTopicPayload = {
    __typename?: 'UpdateTopicPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
};

export type UserNode = Node & {
    __typename?: 'UserNode';
    archived?: Maybe<Scalars['Boolean']>;
    createdAt?: Maybe<Scalars['DateTime']>;
    dateJoined: Scalars['DateTime'];
    email: Scalars['String'];
    firstName: Scalars['String'];
    /** The ID of the object */
    id: Scalars['ID'];
    /** Designates whether this user should be treated as active. Unselect this instead of deleting accounts. */
    isActive: Scalars['Boolean'];
    /** Designates whether the user can log into this admin site. */
    isStaff: Scalars['Boolean'];
    /** Designates that this user has all permissions without explicitly assigning them. */
    isSuperuser: Scalars['Boolean'];
    lastLogin?: Maybe<Scalars['DateTime']>;
    lastName: Scalars['String'];
    meetingSet: MeetingNodeConnection;
    password: Scalars['String'];
    pk?: Maybe<Scalars['Int']>;
    secondaryEmail?: Maybe<Scalars['String']>;
    status?: Maybe<UserStatusNode>;
    uid: Scalars['UUID'];
    updatedAt?: Maybe<Scalars['DateTime']>;
    verified?: Maybe<Scalars['Boolean']>;
};

export type UserNodeMeetingSetArgs = {
    after?: InputMaybe<Scalars['String']>;
    before?: InputMaybe<Scalars['String']>;
    createdAt?: InputMaybe<Scalars['DateTime']>;
    date?: InputMaybe<Scalars['DateTime']>;
    fileHash?: InputMaybe<Scalars['String']>;
    filename?: InputMaybe<Scalars['String']>;
    first?: InputMaybe<Scalars['Int']>;
    last?: InputMaybe<Scalars['Int']>;
    mimeType?: InputMaybe<Scalars['String']>;
    offset?: InputMaybe<Scalars['Int']>;
    processed?: InputMaybe<Scalars['Boolean']>;
    processedTaskId?: InputMaybe<Scalars['String']>;
    processingCompleted?: InputMaybe<Scalars['Boolean']>;
    size?: InputMaybe<Scalars['Int']>;
    summarizationCompleted?: InputMaybe<Scalars['Boolean']>;
    summarized?: InputMaybe<Scalars['Boolean']>;
    summarizedTaskId?: InputMaybe<Scalars['String']>;
    summary?: InputMaybe<Scalars['String']>;
    title?: InputMaybe<Scalars['String']>;
    topics?: InputMaybe<Scalars['String']>;
    uid?: InputMaybe<Scalars['UUID']>;
    updatedAt?: InputMaybe<Scalars['DateTime']>;
    uploadedByUser?: InputMaybe<Scalars['ID']>;
};

export type UserNodeConnection = {
    __typename?: 'UserNodeConnection';
    /** Contains the nodes in this connection. */
    edges: Array<Maybe<UserNodeEdge>>;
    /** Pagination data for this connection. */
    pageInfo: PageInfo;
};

/** A Relay edge containing a `UserNode` and its cursor. */
export type UserNodeEdge = {
    __typename?: 'UserNodeEdge';
    /** A cursor for use in pagination */
    cursor: Scalars['String'];
    /** The item at the end of the edge */
    node?: Maybe<UserNode>;
};

export type UserStatusNode = Node & {
    __typename?: 'UserStatusNode';
    archived: Scalars['Boolean'];
    createdAt?: Maybe<Scalars['DateTime']>;
    /** The ID of the object */
    id: Scalars['ID'];
    secondaryEmail?: Maybe<Scalars['String']>;
    uid: Scalars['UUID'];
    updatedAt?: Maybe<Scalars['DateTime']>;
    user: UserNode;
    verified: Scalars['Boolean'];
};

export type VerifyAccountInput = {
    clientMutationId?: InputMaybe<Scalars['String']>;
    token: Scalars['String'];
};

export type VerifyAccountPayload = {
    __typename?: 'VerifyAccountPayload';
    clientMutationId?: Maybe<Scalars['String']>;
    errors?: Maybe<Scalars['ExpectedErrorType']>;
    success?: Maybe<Scalars['Boolean']>;
    token?: Maybe<Scalars['String']>;
    user?: Maybe<UserNode>;
};
